from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    pre = """
<!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-WEKFJ1L7K3"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-WEKFJ1L7K3');
</script>
"""
    return pre + "Hello World"
    
   
