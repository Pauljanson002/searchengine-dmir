from flask import Flask, render_template, request
from query import search, matched_search, wildcard_search
from elasticsearch_dsl import Index

app = Flask(__name__,template_folder='templates')



@app.route('/', methods=['GET', 'POST'])
def hello_world():
    import pdb
    # pdb.set_trace()
    # return "hello world"
    if request.method == 'POST':
        
        query = request.form['searchTerm']
        fields = {}
 
        Composer = {
            "arrahman" : "ஏ. ஆர். ரஹ்மான்",
            "harris" : "ஹாரிஸ் ஜெயராஜ்",
        }
        Lyricist = {
            "vairamuthu" : "வைரமுத்து",
            "vaali" : "வாலி",
            "na.muthukumar" : "நா. முத்துக்குமார்",
            "damarai" : "தாமரை",
            "yugaparathi" : "யுக பாரதி"
        }
        Singer = {
            "karthik" : "கார்த்திக்",
            "shreya" : "ஸ்ரேயா கோஷல்",
            "naresh" : "நரேஷ் ஐயர்",
            "bala" : "பாலசுப்ரமணியம்"
        }



        if request.form['Composer'] != 'none':
            fields["Composer"] = Composer[request.form['Composer']]
        if request.form['Lyricist'] != 'none':
            fields["Lyricist"] = Lyricist[request.form['Lyricist']]
        if request.form['Singer'] != 'none':
            fields["Singer"] = Singer[request.form['Singer']]

        res = matched_search(fields)
        
        print(request.form.get('basic'))
        if request.form['basic'] == 'Basic':
            res = search(query)
            fields = query
        elif request.form['basic'] ==  'Advanced':
            res = wildcard_search(query)
            fields = query
        else:
            res = matched_search(fields)
        


        
        hits = res['hits']['hits']
        time = res['took']

        num_results =  res['hits']['total']['value']

        return render_template('main.html', query=fields, hits=hits, num_results=num_results,time=time)

    if request.method == 'GET':

        return render_template('main.html', init='True')


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)