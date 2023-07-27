import os.path

from flask import Flask, request, jsonify
from deepface import DeepFace

app = Flask(__name__)

mimetypes_accepted = ['image/png', 'image/jpeg', 'image/jpg', 'application/octet-stream']


@app.route('/api/v1/face/compare', methods=['POST'])
def compare_face():
    base_path = './images/'
    try:
        selfie = request.files['selfie']
        document = request.files['document']

        if selfie.mimetype not in mimetypes_accepted and document.mimetype not in mimetypes_accepted:
            return jsonify({
                'error': True,
                'data': False,
                'code': 1,
                'type': 'Error',
                'msg': 'La imagen cargada debe tener formato: jpeg, jpg o png'
            }), 202
        path_selfie = base_path + selfie.filename
        if os.path.exists(path_selfie):
            os.remove(path_selfie)
        selfie.save(path_selfie)
        selfie.close()

        path_document = base_path + document.filename
        if os.path.exists(path_document):
            os.remove(path_document)
        document.save(path_document)
        document.close()

        resul = DeepFace.verify(img1_path=path_selfie, img2_path=path_document, model_name='Facenet512',
                                distance_metric='euclidean', detector_backend='opencv')

        os.remove(path_selfie)
        os.remove(path_document)
        if resul['verified']:
            resul['verified'] = 'true'
        else:
            resul['verified'] = 'false'

        return jsonify({
            'error': False,
            'data': resul,
            'code': 22,
            'type': 'success',
            'msg': 'Procesado correctamente'
        }), 200

    except Exception as e:
        return jsonify({
            'error': False,
            'data': False,
            'code': 22,
            'type': 'error',
            'msg': 'Ocurrio un error a la hora comparar las caras, error: ' + str(e)
        }), 202


if __name__ == '__main__':
    from waitress import serve

    print('Server on port: ', 5006)
    serve(app, host="0.0.0.0", port=5006)
