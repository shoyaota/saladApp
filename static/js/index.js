$(function(){

    $('#selectedImage').change(function(e) {
        var files = e.target.files; 
        console.log(files);
      });

})