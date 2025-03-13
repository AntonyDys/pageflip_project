window.addEventListener('beforeunload', function (event) {
    event.preventDefault();
    event.returnValue = 'Are you sure you want to leave this page? Plenty of books await.'; 
});


