// Adiciona o evento de click ao botão de toggle
document.querySelector('.toggle-btn').addEventListener('click', function() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('collapsed');
    
    const toggleBtn = document.querySelector('.toggle-btn span');
    if (sidebar.classList.contains('collapsed')) {
      toggleBtn.innerHTML = '&#9654;';  // Triângulo apontando para a direita
    } else {
      toggleBtn.innerHTML = '&#9664;';  // Triângulo apontando para a esquerda
    }
  });
  
  // Controla o submenu
  document.querySelectorAll('.has-submenu > a').forEach(item => {
    item.addEventListener('click', function(e) {
      e.preventDefault(); // Impede o link de ser seguido
      const parent = item.parentElement;
      parent.classList.toggle('open'); // Alterna o estado de "aberto"
    });
  });
  