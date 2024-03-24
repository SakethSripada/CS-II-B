function createX(item) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7"); // Unicode character for "x"
  span.className = "close"; // needed for CSS access
  span.appendChild(txt);
  item.appendChild(span);
}

// Add an 'x' at the end of each list item
var itemList = document.getElementsByTagName("LI");
var i;
for (i = 0; i < itemList.length; i++) {
  createX(itemList[i]);
}

// Click on close button to delete a list item
function deleteItem() {
  var buttons = document.getElementsByClassName("close");
  var i;
  for (i = 0; i < buttons.length; i++) {
    buttons[i].onclick = function() {
      var box = this.parentElement;
      box.style.display = "none";
    }
  }
}

deleteItem();

// Add check mark when an item has been clicked
var list = document.querySelector('ul');
list.addEventListener('click', function(event) {
  if (event.target.tagName === 'LI') {
    event.target.classList.toggle('checked');
  }
}, false);

// Create Add button Functionality
function newItem() {
  var li = document.createElement("li");
  var userInput = document.getElementById("newItem").value;
  var text = document.createTextNode(userInput);
  li.appendChild(text);
  if (userInput === '') {
    alert("You cannot submit a blank item!");
  } else {
    document.getElementById("myList").appendChild(li);
  }
  document.getElementById("newItem").value = "";

  createX(li);
  deleteItem();
}
