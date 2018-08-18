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

	document.getElementById("startButton").onclick = null;
	let canvas = document.createElement('canvas');
	let ctx = canvas.getContext('2d');
	canvas.width = document.querySelector('video').width+21
  	canvas.height = document.querySelector('video').height-40;
  	console.log(canvas.width)

  	ctx.drawImage(localVideo, 0, 0, canvas.width, canvas.height);

  	document.getElementById("video_canvas").appendChild(canvas);
  	console.log(document.getElementById("video_canvas"));
  	document.getElementById("video_canvas").removeChild(document.querySelector('video'));

  	canvas.toBlob(makeBlob, 'image/jpeg', .9);


}

function makeBlob(blob){

    var formdata = new FormData();
    console.log(blob)

	formdata.append('nutrient_info',blob);

	fetch('http://127.0.0.1:5000/nutrihack_api', {
        method: 'POST',
        mode: 'no-cors',
		body: formdata
	})
	.then(response => response.json())
	.catch(error => console.log('Error: ', error))
	.then(response => console.log('Success: ', response))
}
