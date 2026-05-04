function checkboxToggle(checkbox, url){
  var checkBox = checkbox;
  if (checkBox.checked == true){
    window.location.href = url + "&checked=True"

  } else {
    window.location.href = url + "&checked=False"
  }
}
