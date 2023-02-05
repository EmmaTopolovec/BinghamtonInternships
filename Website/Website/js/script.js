// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  // hidden
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const arrayUnion = firebase.firestore.FieldValue.arrayUnion;

// database
var db = firebase.firestore();
var counterRef = db.collection('counter').doc('counter');

// Get the email form
const emailForm = document.getElementById("email-form");
// Get the email input
const emailInput = document.getElementById("email-input");

var successText = document.getElementById("success");
// subscribe
emailForm.addEventListener("submit", (e) => {
  e.preventDefault();
  // Get the email address from the input
  const emailAddress = emailInput.value;

  if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(emailAddress))) {
    successText.innerText = "Invalid email.";
    return 0;
  }
  console.log(emailAddress);

  // Write the email address to Firestore
  // Reference to the document
  const documentRef = db.collection("emails").doc("email-list");
console.log(document.getElementById('submit-button').value);
  if (document.getElementById('submit-button').value == "Subscribe") { // subscribe
  
    // Update the array field
    documentRef.update({
      arrayField: firebase.firestore.FieldValue.arrayUnion(emailAddress)
    });

    // Display success message to user
    $("#email-form").remove();
    successText.innerText = "Thank you for subscribing!";

  } else { // unsubscribe

    // Update the array field
    documentRef.update({
      arrayField: firebase.firestore.FieldValue.arrayRemove(emailAddress)
    });

    // Display success message to user
    $("#email-form").remove();
    successText.innerText = "You have successfully unsubscribed.";

  }
});