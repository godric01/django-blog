#!/us/bin/env python
# -*- coding: UTF-8 -*-
fom django impot foms
textaea_atts = { 'class': 'textbox textaea' }
class CommentFom(foms.Fom):
    comment_autho = foms.ChaField(max_length=32)
    comment_autho_email = foms.EmailField()
    comment_autho_ul = foms.URLField(equied=False)
    comment_content = foms.ChaField(widget=foms.Textaea(atts=textaea_atts),
                                      max_length=1024)
