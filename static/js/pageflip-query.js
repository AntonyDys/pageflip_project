window.addEventListener('beforeunload', function (event) {
    event.preventDefault();
    event.returnValue = 'Are you sure you want to leave this page? Plenty of books await.'; 
});

//highlighting stuff when the cursor is over it - don't know if this works

document.querySelectorAll('.highlightable').forEach(function(element) {
    element.addEventListener('mouseover', function() {
        element.style.backgroundColor = 'purple'; 
    });
    
    element.addEventListener('mouseout', function() {
        element.style.backgroundColor = ''; 
    });
});
