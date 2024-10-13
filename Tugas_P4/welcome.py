from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/karyawan', methods=['GET', 'POST', 'PUT', 'DELETE'])
def karyawan():
    try:
        if request.method == 'GET':
            data = [{
                'nama': 'Indra',
                'pekerjaan': 'Web Engineer',
                'usia': '27',
            }]
        elif request.method == 'POST':
            data = [{
                'nama': 'Galih',
                'pekerjaan': 'Cyber Security',
                'usia': '22',
            }]
        elif request.method == 'PUT':
            data = [{
                'nama': 'Putri',
                'pekerjaan': 'UI/UX Designer',
                'usia': '20',
            }]
        else:
            data = [{
                'nama': 'Lukman',
                'pekerjaan': 'Web Engineer',
                'usia': '24',
            }]
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    
    return make_response(jsonify({'data': data}), 200)

if __name__ == '__main__':
    app.run()
