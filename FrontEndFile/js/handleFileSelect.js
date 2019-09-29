/*

function handleFileSelect() 
{
  var files = document.getElementById('up-image').files[0]; //파일 객체
  var reader = new FileReader();

  //파일정보 수집       
  reader.onload = (function(theFile) 
  {
    return function(e) 
    {
      //이미지 뷰
      var img_view = ['<img src="', e.target.result, '" title="', escape(theFile.name), '"/>'].join('');                
      document.getElementById('up-image-list').innerHTML = img_view;
    };
  })(files);
  reader.readAsDataURL(files);    
}

*/

var sel_file;

$(document).ready(function() {
  $("#input_img").on("change", handleImgFileSelect);
});

function handleImgFileSelect(e){
  var files = e.target.files;
  var filesArr = Array.prototype.slice.call(files);

  filesArr.forEach(function(f) {
    if(!f.type.match("image.*")) {
      alert("확장자는 이미지 확장자만 가능합니다.");
      return;
    }

    sel_file = f;

    var reader = new FileReader();
    reader.onload = function(e) {
      $("#img").attr("src", e.target.result);
    }
    reader.readAsDataURL(f);
  });
}