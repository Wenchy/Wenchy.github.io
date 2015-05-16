# -*- encoding: utf-8 -*-
import os
import sys
import codecs
import re

# encoding=utf-8
reload(sys)
sys.setdefaultencoding("utf-8")

class pygen():
	def __init__(self):
		# markdowns and blogs directories
		root_dir = os.path.split(os.getcwdu())[0]
		self.md_dir = os.path.join(root_dir, u"markdowns")
		self.blog_dir = os.path.join(root_dir, u"blogs")
		self.abs_layout_default_filepath = os.path.join(self.blog_dir, u'_layouts', u'default.tpl.html')
		self.abs_layout_index_filepath = os.path.join(self.blog_dir, u'_layouts', u'index.tpl.html')
		self.abs_index_filepath = os.path.join(root_dir, u'index.html')
		# all markdown files
		self.md_files = [x for x in os.listdir(self.md_dir) if not os.path.isdir(x) and os.path.splitext(x)[1] == '.md']

	def replace_html_tpl_keyword(self, match):
		if match.group(0).startswith('@include'):
			p = re.compile(ur'\.')
			path_list = p.split(match.group(1))
			path_list[-1] += '.tpl.html'
			# print path_list
			abs_filename = os.path.join(self.blog_dir, *path_list)
			with open(abs_filename, "r") as f:
				return f.read()
		elif match.group(0).startswith('{{'):
			if match.group(1) == 'markdown.url':
				return '../markdowns/'+self.cur_md_filename
			elif match.group(1) == 'blog.title':
				return self.cur_md_filename.replace('.md', '')
			elif match.group(1) == 'blog.list':
				md_files_string = ''
				reverse_md_files = sorted(self.md_files, reverse=True)
				for filename in reverse_md_files:
					p = re.compile(ur'-')
					item_list = p.split(filename.replace('.md', ''))
					# print item_list
					post_url = 'blogs/' + filename.replace('md', 'html')
					post_time = '-'.join(item_list[0:3])
					post_title = ' '.join(item_list[3:])
					# print post_time
					md_files_string += '<dt>'+post_time+'</dt><dd>'+ '<a href="'+post_url+'">'+post_title+'</a></dd>\n'
				return md_files_string

	def render_tpl(self, abs_tpl_filename):
		with open(abs_tpl_filename, "r") as f:
			tpl_string = f.read()
			# replace keywords like "@include('keyword')"
			include_pattern = re.compile(ur'@include\([\'|\"]([\w|.]+)[\'|\"]\)')
			layout_string = include_pattern.sub(self.replace_html_tpl_keyword, tpl_string)
			# replace keywords like "{{ keyword }}"
			brace_pattern = re.compile(ur'{{ *([\w|.]+) *}}')
			html_string = brace_pattern.sub(self.replace_html_tpl_keyword, layout_string)
			return html_string

	# render markdowns to blogs
	def blogs_create(self, abs_tpl_filename):
		for md_filename in self.md_files:
			self.cur_md_filename = md_filename
			# blog file
			abs_md_filename = os.path.join(self.md_dir, md_filename)
			abs_blog_filename = os.path.join(self.blog_dir, os.path.splitext(md_filename)[0]+'.html')
			with open(abs_blog_filename, "w") as blog_file:
				blog_file.write(self.render_tpl(abs_tpl_filename))

	# render index.tpl.html to index.html
	def index_create(self, abs_tpl_filename):
		with open(self.abs_index_filepath, "w+") as index_file:
			index_file.write(self.render_tpl(abs_tpl_filename))

	# render index.tpl.html to index.html
	def page_generation(self):
		self.blogs_create(self.abs_layout_default_filepath)
		self.index_create(self.abs_layout_index_filepath)

# match = re.search(ur'{{ *([\w|.]+) *}}', u'dd@include("_partials.asset") {{  mm_g }} world! @include(\'ddd.asset\') @include("eee.asset") @include(\'ddrffd.asset\') ')
# print match.group(0).startswith('{{')

if __name__ == '__main__':
	mypygen = pygen()
	mypygen.page_generation()