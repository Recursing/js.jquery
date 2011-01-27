from fanstatic import Library, Resource

library = Library('jquery', 'resources')

# CDN info from http://docs.jquery.com/Downloading_jQuery#CDN_Hosted_jQuery

_jquery_minified = Resource(library, 'jquery.min.js', cdns={
    'google': '//ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js',
    'microsoft': '//ajax.aspnetcdn.com/ajax/jQuery/jquery-1.4.4.min.js',
    'jquery': '//code.jquery.com/jquery-1.4.4.min.js',
})

jquery = Resource(library, 'jquery.js', minified=_jquery_minified, cdns={
    'google': '//ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.js',
    'microsoft': '//ajax.aspnetcdn.com/ajax/jQuery/jquery-1.4.4.js',
    'jquery': '//code.jquery.com/jquery-1.4.4.js',
})
