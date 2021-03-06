# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2012, 2013, 2014, 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from zope.interface import Interface
from zope.schema import TextLine, ASCIILine, Field


class INavLinksContentProvider(Interface):
    topicTitle = TextLine(
        title="Title of the Topic",
        description='The title of the topic.',
        required=True)

    relatedPosts = Field(
        title='Related Posts',
        description='The posts in the same topic.',
        required=True)

    pageTemplateFileName = ASCIILine(
        title="Page Template File Name",
        description="""The name of the ZPT file
        that is used to render the post.""",
        required=False,
        default=b'browser/templates/navlinks.pt')
