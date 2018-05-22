import sys

from gack.web import app

port = 8080
use_reloader = False
for arg in sys.argv[1:]:
    if '--port' in arg:
        port = int(arg.split('=')[1])
    elif '--use_reloader' in arg:
        use_reloader = arg.split('=')[1] == 'true'

# threaded to fix broken pipe error if request fails
# also slightly faster at reporting fails
app.run(host='0.0.0.0', port=port, debug=True, use_reloader=use_reloader,
        threaded=True)
