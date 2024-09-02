//dark mode
document.getElementById('toggle-dark-mode').addEventListener('click', function() {
  document.body.classList.toggle('dark-mode');
  document.getElementById('header').classList.toggle('dark-mode');
  document.querySelectorAll('.nav-link').forEach(link => link.classList.toggle('dark-mode'));
  document.querySelectorAll('.card').forEach(card => card.classList.toggle('dark-mode'));

  //changing icon
  if (document.body.classList.contains('dark-mode')) {
    document.getElementById('icon').src = "static/images/light_mode.png";
  } else {
    document.getElementById('icon').src = "static/images/dark_mode.png";
  }

  // local storage
  if (document.body.classList.contains('dark-mode')) {
    localStorage.setItem('theme', 'dark');
  } else {
    localStorage.setItem('theme', 'light');
  }
});

// after loading, still stay
document.addEventListener('DOMContentLoaded', () => {
  const theme = localStorage.getItem('theme');
  if (theme === 'dark') {
    document.body.classList.add('dark-mode');
    document.getElementById('header').classList.add('dark-mode');
    document.querySelectorAll('.nav-link').forEach(link => link.classList.add('dark-mode'));
    document.querySelectorAll('.card').forEach(card => card.classList.add('dark-mode'));
    document.getElementById('icon').src = "static/images/light_mode.png";
  } else {
    document.getElementById('icon').src = "static/images/dark_mode.png";
  }
});

//toggle button 
const menuToggle = document.getElementById('menu-toggle');
  const navMenu = document.getElementById('nav-menu');

  menuToggle.addEventListener('click', () => {
    navMenu.classList.toggle('hidden');
  });