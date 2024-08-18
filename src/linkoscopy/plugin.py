# TODO - delete this file
# # THis was intended to implement an MkDocs plugin.
#  instead it should be standalone CLI utility


# import logging
# from pathlib import Path
# from mkdocs.config import config_options
# from mkdocs.plugins import BasePlugin

# from . import link_validator


# #  TODO

# log = logging.getLogger("mkdocs")


# class LinkChecker(BasePlugin):
#     # style is added to the image tag.  e.g. margin-right:10px;
#     config_scheme = (("style", config_options.Type(str, default="")),)

#     def on_pre_build(self, **kwargs):
#         pass

#     # This is done for each page.  The markdown conversion has been done at this point.
#     def on_page_content(self, html, **kwargs):
#         pass

#     def on_post_build(self, **kwargs):
#         pass
