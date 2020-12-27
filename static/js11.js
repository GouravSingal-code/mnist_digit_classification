// wait for the content of the window element
// to load, then performs the operations.
// This is considered best practice.
window.addEventListener('load', ()=>{

    //console.log(10);
    resize(); // Resizes the canvas once the window loads
    document.addEventListener('mousedown', startPainting);
    document.addEventListener('mouseup', stopPainting);
    document.addEventListener('mousemove', sketch);
    window.addEventListener('resize', resize);

});

const canvas = document.querySelector('#mycanvas');

// Context for the canvas for 2 dimensional operations
const ctx = canvas.getContext('2d');
//ctx.scale(0.1 ,0.1);

// Resizes the canvas to the available size of the window.
function resize(){
  //ctx.scale(0.1 ,0.1);
  ctx.canvas.width = 320;
  ctx.canvas.height = 320;

  ctx.beginPath();
  var rect = ctx.rect(20 , 20 , 280 , 280 );
  ctx.fillStyle = "black";
  ctx.fill();
}



// Stores the initial position of the cursor
let coord = {x:0 , y:0};

// This is the flag that we are going to use to
// trigger drawing
let paint = false;

// Updates the coordianates of the cursor when
// an event e is triggered to the coordinates where
// the said event is triggered.
function getPosition(event){
  coord.x = event.clientX - canvas.offsetLeft;
  coord.y = event.clientY - canvas.offsetTop;
}

// The following functions toggle the flag to start
// and stop drawing
function startPainting(event){
  paint = true;
  getPosition(event);
}
function stopPainting(){
  paint = false;
}

function sketch(event){
  if (!paint) return;
  ctx.beginPath();

  ctx.lineWidth = 10;

  // Sets the end of the lines drawn
  // to a round shape.
  ctx.lineCap = 'round';

  ctx.strokeStyle = 'white';

  // The cursor to start drawing
  // moves to this coordinate
  ctx.moveTo(coord.x, coord.y);

  // The position of the cursor
  // gets updated as we move the
  // mouse around.
  getPosition(event);

  // A line is traced from start
  // coordinate to this coordinate
  ctx.lineTo(coord.x , coord.y);

  // Draws the line.
  ctx.stroke();

}


$(document).ready(function(){
  $("#test").click(function(){


      var ImageData =  ctx.getImageData( 20 , 20 ,  280 , 280 );

    //  console.log(ImageData.data);
      //resizeImageData(ImageData, 28 , 28);
    //  ImageData.scale(0.1 , 0.1)

      let pixel_array = [];

      for( let i=0 ; i<78400 ; i++ ){
          pixel_array.push(ImageData.data[i*4]);
      }

      //console.log(pixel_array.length)


      fetch('/pixel_array' , {
        method:'POST',
        enctype:'multipart/form-data',
        headers:{
         'Accept':'application/json , text/plain , text/html */*',
         'Content-type':'application/json'
       },
        body:JSON.stringify({array:pixel_array})
      })
      .then(res=>res.text())
      .then(data=>{
          let x = 1;
         var counter = setInterval(function(){

          if( x<2 ){
          document.getElementById("no").innerHTML = "..." ;
        }

          if( x == 2 ){
            document.getElementById("no").innerHTML = data;
            clearInterval(counter);
          }
          x++;
        },1000);

  })

})

  $("#clear").click(function(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);

      ctx.beginPath();
      var rect = ctx.rect(20 , 20 , 280 , 280 );
      ctx.fillStyle = "black";
      ctx.fill();
      document.getElementById("no").innerHTML = " ";
  })

})
