function sayHi() {
    alert("Hello");
  }
  
  // global functions are methods of the global object:
  window.sayHi();
  alert(window.innerHeight)

  document.body.style.background = "red";

  setTimeout(() => document.body.style.background="", 1000);

