from fanstatic import Library, Resource

library = Library('jquery', 'resources')

# CDN info from http://docs.jquery.com/Downloading_jQuery#CDN_Hosted_jQuery

_jquery_minified = Resource(library, 'jquery.min.js', cdns={
    ('google', 'http'): 'http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js',
    ('google', 'https'): 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js',
    ('microsoft', 'http'): 'http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.4.4.min.js',
    ('microsoft', 'https'): 'https://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.4.4.min.js',
    ('jquery', 'http'): 'http://code.jquery.com/jquery-1.4.4.min.js',
})

jquery = Resource(library, 'jquery.js', minified=_jquery_minified, cdns={
    ('google', 'http'): 'http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.js',
    ('google', 'https'): 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.js',
    ('microsoft', 'http'): 'http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.4.4.js',
    ('microsoft', 'https'): 'https://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.4.4.js',
    ('jquery', 'http'): 'http://code.jquery.com/jquery-1.4.4.js',
})
