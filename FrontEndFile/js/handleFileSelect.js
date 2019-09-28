function handleFileSelect() 
{
  var files = document.getElementById('up_files').files[0]; //파일 객체
  var reader = new FileReader();

  //파일정보 수집        
  reader.onload = (function(theFile) 
  {
    return function(e) 
    {
      //이미지 뷰
      var img_view = ['<img src="', e.target.result, '" title="', escape(theFile.name), '"/>'].join('');                
      document.getElementById('list').innerHTML = img_view;
    };
  })(files);
  reader.readAsDataURL(files);    
}