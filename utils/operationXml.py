# coding:utf-8
import os
import xml.dom.minidom

class OpeartionXml(object):
    def dir_base(self,filename,filepath="data"):
        '''
        获取data文件夹下的内容
        :param filename: 文件名
        :param filepath: 路径
        :return:
        '''
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), filepath, filename)

    def getXmlData(self, value):
        """
        获取xml中的单节点数据
        :param value:
        :return:
        """
        dom = xml.dom.minidom.parse(self.dir_base("ui.xml"))
        db = dom.documentElement
        name = db.getElementsByTagName(value)
        nameValue = name[0]
        return nameValue.firstChild.data

    def getXmlUser(self, parent, child):
        """
        获取xml中的子节点数据
        :param parent:
        :param chile:
        :return:
        """
        dom = xml.dom.minidom.parse(self.dir_base("ui.xml"))
        db = dom.documentElement
        itemlist = db.getElementsByTagName(parent)
        item = itemlist[0]
        return item.getAttribute(child)