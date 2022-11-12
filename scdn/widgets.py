from django import forms


class VersionWidget(forms.TextInput):
    class Media:
        # css = {
        # 'all': ('pretty.css',)
        # }
        js = ('js/imask.js', 'js/version_mask.js',)

    def __init__(self, attrs=None):
        attrs = {'class': 'version-field', **(attrs or {})}
        super().__init__(attrs=attrs)
