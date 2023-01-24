import datetime
from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())


@app.route('/profile')
def profile():
    return render_template('profile.html', utc_dt=datetime.datetime.utcnow())



@app.route('/search')
def search():
    users = get_profiles_all()
    return render_template('search_list.html', utc_dt=datetime.datetime.utcnow(),data=users,size=len(users))

@app.route('/test')
def test():
    return render_template('landing_page.html')


@app.route('/search_by_filter', methods=['POST'])
def search_by_filter():
    keyword = request.form['keyword']
    print(keyword)
    users = filter_profiles(keyword.lower())
    return render_template('search_list.html', utc_dt=datetime.datetime.utcnow(),data=users,size=len(users))

@app.route('/go_profile', methods=['POST'])
def go_profile():
    # info = request.form['go_profile']
    # print(request)
    # print(info)
    print(request.form)
    # return 'ok'
    return render_template('profile.html', utc_dt=datetime.datetime.utcnow())



def filter_profiles(keyword):
    users = get_profiles_all()
    new_users = []
    for p in users:
        if keyword in p['name'].lower():
            new_users.append(p)
    return new_users

def get_profiles_all():
    users = [{'name':'Omer O','gender':'Male','last_visit':'2022-06-12','location':'Istanbul','branch':'Pendik Medipol Hastanesi'},
             {'name': 'Rana R','gender':'Female', 'last_visit': '2023-01-02', 'location': 'Istanbul','branch':'Çamlica Medipol Hastanesi'},
             {'name': 'Malek M','gender':'Male', 'last_visit': '2021-02-23', 'location': 'Istanbul','branch':'Bağcilar Medipol Hastanesi'},
             {'name': 'Merve M','gender':'Female', 'last_visit': '2022-09-29', 'location': 'Istanbul','branch':'Esenler Medipol Hastanesi'}]
    return users

if __name__ == '__main__':
    app.run(debug = True,port=5005)
