function contact(){
  var hello = document.getElementById("form-name").value;
  console.log('Contact form submitted');
  console.log(document.getElementById('contactform'))
  alert('Thank you for submitting your message, '+ hello +'. We will be in touch soon.');
  return 'Contact form submitted';
}
