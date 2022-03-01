from flask import Flask, escape, request, render_template
import pickle


model=pickle.load(open("model.pkl","rb"))

vector= pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prediction", methods=['GET','POST'])
def prediction():
    if request.method=='POST':
        comment=request.form['comment']
        predict= model.predict(vector.transform([comment]))
        print(predict)

        if predict== 0:
            predict = "Not an Advertisment."
        else:
            predict ="Advertisement."

        return render_template("prediction.html", prediction_text="The comment is -> {}".format(predict))

    else: 
        return render_template("prediction.html")


if __name__== '__main__':
    app.run()