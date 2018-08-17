'use strict';

const mediaStreamConstraints = {
  video: true,
};

const localVideo = document.querySelector('video');

let localStream;

function gotLocalMediaStream(mediaStream) {
  localStream = mediaStream;
  localVideo.srcObject = mediaStream;
 
 }

function handleLocalMediaStreamError(error) {
  console.log('navigator.getUserMedia error: ', error);
}

navigator.mediaDevices.getUserMedia(mediaStreamConstraints)
  .then(gotLocalMediaStream).catch(handleLocalMediaStreamError);

document.getElementById("startButton").addEventListener("click", MakeImage);

function MakeImage(){

    let canvas = document.createElement('canvas');
    let ctx = canvas.getContext('2d');
    canvas.width = 200;
      canvas.height = 200;
      console.log(canvas.width)

      ctx.drawImage(localVideo, 0, 0, canvas.width, canvas.height);

      document.getElementById("video_canvas").appendChild(canvas);
      console.log(document.getElementById("video_canvas"));
      document.getElementById("video_canvas").remove(document.getElementById("video_canvas").childNodes[0]);


}

function makeBlob(blob){

    gotLocalMediaStream(blob);
}
