from flask import render_template, flash, redirect
from flask import Flask
from flask import request
from forms import WeatherForm
from demo_3w_task import fetchWeather

app = Flask(__name__)
app.config.from_object('config')
record = []

@app.route('/', methods=['GET', 'POST'])
def Weather_web():
    weather = {}
    form = WeatherForm()
    #if form.validate_on_submit():
    if request.method == 'POST' and form.validate():
       if request.form['submit'] == "查询":
           status,info = fetchWeather(form.city.data)
           if status == 200:
               weather['city'] = form.city.data
               weather['text'] = info['results'][0]['now']['text']
               weather['temperature'] = info['results'][0]['now']['temperature']
               record.append(weather)
               error = 0
           else:
               error = 1
           return render_template('WeatherQuery.html',
                                   form=form,
                                   weather=weather,
                                   error = error)
       elif request.form['submit'] == "历史":
           return render_template('WeatherHistroy.html',
                                   form=form,
				   record = record)
       elif request.form['submit'] == "帮助":
           return render_template('Weatherhelp.html',
				   form=form)

    return render_template('WeatherIndex.html', 
                           form=form)



if __name__ == "__main__":
    app.run()

