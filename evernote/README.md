## evernote2zim ##

**evernote2zim.py** 是一个将Evernote里的共享链接批量处理成zim里的超链接格式的脚本。如果你是一个Zim Desktop Wiki用户，同时在Evernote里生成了很多共享链接，你想提取这些共享链接以及其标题，然后以超链接的格式导入到Zim里，那么可以试试这个脚本。

###用法###
1. 将evernote里的共享链接导出到一个文件SharedLinks.txt；
2. 将evernote里的共享文章以html的格式导出，至Evernote.html；
3. 将上面两个文件与evernote2zim.py放至同一目录，执行evernote2zim.py；
4. 执行结束后会生成一个evernote.txt文件，可以将其放至zim的Notebook目录下，或者将其内容追加至你指定的某个zim笔记本。

###效果###
最后在Zim里的效果如下：

![](https://github.com/hiqhan/tools/blob/master/evernote/showninzim.PNG)

##evernote2zim##
**evernote2zim.py** is a script for converting shared links from evernote into links in Zim Desktop Wiki. If you are a Zim Desktop Wiki user as well as a Evernote user, you could try this script if you would like to extract the shared links with titles into links format in Zim Desktop Wiki.

##Usage##
1. Extract shared links from evernote into a file named SharedLinks.txt;
2. Extract shared posts from evernote into a html file named Evernote.html;
3. Put SharedLinks.txt, Evernote.html into the directory where evernote2zim.py locates, excute the script;
4. Then a file called evernote.txt would appear in the same directory, put it into Zim Notebook directory or append it to the specific Notebook file.  

##Result##
The image following shows result in Zim:

![](https://github.com/hiqhan/tools/blob/master/evernote/showninzim.PNG)
