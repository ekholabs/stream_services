from helpers.FFMpegHelper import FFMpeg

from flask import Flask, Blueprint, jsonify, make_response, request, abort, redirect

import logging
import json

ffmpeg_service = Blueprint('ffmpeg_service', __name__)

@ffmpeg_service.route('/streamDetails', methods=['POST'])
def stream_details():
    data = request.json
    ffmpeg = FFMpeg()
    streams = ffmpeg.extract_stream_details(data['url'])

    return make_response(jsonify(streams))

@ffmpeg_service.errorhandler(400)
def bad_request(erro):
    return make_response(jsonify({'error': 'We cannot process the file sent in the request.'}), 400)

@ffmpeg_service.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Resource no found.'}), 404)
