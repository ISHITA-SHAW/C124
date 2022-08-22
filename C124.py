from flask import Flask,jsonify,request
app = Flask(__name__)

tasks = [
    {
        'id':1,
        'title':u'buy',
        'description':u'facewash,snacks',
        'done':False
    },
    {
        'id':2,
        'title':u'learn',
        'description':u'mathematics,physics',
        'done':False
    }
]
@app.route("/")
def home():
    return 'Hello World'

@app.route('/getdata')
def getdata():
    return jsonify({
        "data":tasks
    })

@app.route('/adddata',methods = ['POST'])
def adddata():
    if not request.json:
        return jsonify({
            "message":'please provide data'
        })
    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
        
    }
    tasks.append(task)
    return jsonify({
            "message":'successful'
        })
if(__name__=="__main__"):
    app.run()

