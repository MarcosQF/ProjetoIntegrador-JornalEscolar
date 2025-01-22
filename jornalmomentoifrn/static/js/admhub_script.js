document.querySelector('.toggle-btn').addEventListener('click', function() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('collapsed');
    
    const toggleBtn = document.querySelector('.toggle-btn span');
    if (sidebar.classList.contains('collapsed')) {
      toggleBtn.innerHTML = '&#9654;';  
    } else {
      toggleBtn.innerHTML = '&#9664;';  
    }
  });
  
 
  document.querySelectorAll('.has-submenu > a').forEach(item => {
    item.addEventListener('click', function(e) {
      e.preventDefault(); 
      const parent = item.parentElement;
      parent.classList.toggle('open'); 
    });
  });
  