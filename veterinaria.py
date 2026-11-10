# ==========================================
# Generador de Archivos Web - Patitas Felices
# Guardar y ejecutar en Python como 'generar_veterinaria.py'
# ==========================================

# 1. Contenido para 'index.html'
html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Veterinaria Patitas Felices - Reserva de Citas</title>
    <!-- Google Fonts & Font Awesome Icons -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- CSS Externo -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <!-- Header Navigation -->
    <header>
        <div class="navbar">
            <a href="#" class="logo">
                <i class="fa-solid fa-paw"></i> Patitas Felices
            </a>
            <nav>
                <a href="#servicios">Servicios</a>
                <a href="#veterinarios">Veterinarios</a>
                <a href="#reserva" class="nav-btn">Reservar Cita</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>Cuidado con amor para tu mejor amigo</h1>
            <p>Agenda una consulta médica, baño o vacuna de manera rápida y sin saturar nuestras líneas telefónicas.</p>
            <a href="#reserva" class="btn-primary">Apartar una Cita</a>
        </div>
    </section>

    <!-- Contenido Principal -->
    <main class="main-container">
        
        <!-- Sección de Servicios -->
        <section id="servicios" class="section">
            <h2 class="section-title">Nuestros Servicios</h2>
            <p class="section-subtitle">Atención integral y profesional para tu mascota</p>
            <div class="service-grid" id="service-grid">
                <!-- Dinámico vía script.js -->
            </div>
        </section>

        <!-- Sección de Veterinarios -->
        <section id="veterinarios" class="section">
            <h2 class="section-title">Nuestros Especialistas</h2>
            <p class="section-subtitle">Conoce al equipo médico encargado del bienestar animal</p>
            <div class="vet-grid" id="vet-grid">
                <!-- Dinámico vía script.js -->
            </div>
        </section>

        <!-- Sección de Formulario de Reserva -->
        <section id="reserva" class="section">
            <div class="booking-card">
                <h2 class="section-title">Reserva tu Turno</h2>
                <p class="section-subtitle">Selecciona fecha, hora y servicio de preferencia</p>
                
                <form id="booking-form">
                    <div class="form-group">
                        <label for="owner-name"><i class="fa-solid fa-user"></i> Nombre del Propietario</label>
                        <input type="text" id="owner-name" required placeholder="Ej. Juan Pérez">
                    </div>

                    <div class="form-group">
                        <label for="pet-name"><i class="fa-solid fa-dog"></i> Nombre de la Mascota</label>
                        <input type="text" id="pet-name" required placeholder="Ej. Firulais">
                    </div>

                    <div class="form-group">
                        <label for="service-select"><i class="fa-solid fa-stethoscope"></i> Servicio Requerido</label>
                        <select id="service-select" required></select>
                    </div>

                    <div class="form-group">
                        <label for="vet-select"><i class="fa-solid fa-user-doctor"></i> Veterinario de Preferencia</label>
                        <select id="vet-select" required></select>
                    </div>

                    <div class="form-row">
                        <div class="form-group">
                            <label for="appointment-date"><i class="fa-solid fa-calendar"></i> Fecha</label>
                            <input type="date" id="appointment-date" required>
                        </div>
                        <div class="form-group">
                            <label for="appointment-time"><i class="fa-solid fa-clock"></i> Hora</label>
                            <input type="time" id="appointment-time" required>
                        </div>
                    </div>

                    <button type="submit" class="btn-confirm">Confirmar Cita</button>
                </form>

                <!-- Mensaje de éxito oculto inicialmente -->
                <div id="success-message" class="hidden">
                    <i class="fa-solid fa-circle-check"></i>
                    <h3>¡Cita Registrada con Éxito!</h3>
                    <p id="success-details"></p>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 Clínica Veterinaria Patitas Felices - Todos los derechos reservados.</p>
    </footer>

    <!-- JavaScript Externo -->
    <script src="script.js"></script>
</body>
</html>
"""

# 2. Contenido para 'styles.css'
css_content = """:root {
    --primary: #2A9D8F;
    --primary-dark: #21867A;
    --accent: #E9C46A;
    --bg-light: #F4F6F8;
    --text-dark: #264653;
    --text-muted: #6C757D;
    --white: #FFFFFF;
    --card-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

body {
    background-color: var(--bg-light);
    color: var(--text-dark);
    line-height: 1.6;
}

/* Header & Navegación */
header {
    background-color: var(--white);
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 2rem;
}

.logo {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 8px;
}

nav {
    display: flex;
    align-items: center;
    gap: 2rem;
}

nav a {
    text-decoration: none;
    color: var(--text-dark);
    font-weight: 500;
    transition: color 0.3s;
}

nav a:hover {
    color: var(--primary);
}

.nav-btn {
    background-color: var(--primary);
    color: white !important;
    padding: 0.5rem 1.2rem;
    border-radius: 20px;
}

.nav-btn:hover {
    background-color: var(--primary-dark) !important;
}

/* Hero Section */
.hero {
    background: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)), 
                url('https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=1200&q=80') center/cover no-repeat;
    height: 60vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
    padding: 0 1rem;
}

.hero-content {
    max-width: 700px;
}

.hero h1 {
    font-size: 2.8rem;
    margin-bottom: 1rem;
}

.hero p {
    font-size: 1.1rem;
    margin-bottom: 2rem;
    font-weight: 300;
}

.btn-primary {
    background-color: var(--primary);
    color: white;
    padding: 0.8rem 2rem;
    border-radius: 30px;
    font-weight: 600;
    text-decoration: none;
    transition: background 0.3s;
    display: inline-block;
}

.btn-primary:hover {
    background-color: var(--primary-dark);
}

/* Contenedores y Secciones */
.main-container {
    max-width: 1200px;
    margin: 3rem auto;
    padding: 0 2rem;
}

.section {
    margin-bottom: 4rem;
}

.section-title {
    text-align: center;
    font-size: 2rem;
    color: var(--text-dark);
    margin-bottom: 0.5rem;
}

.section-subtitle {
    text-align: center;
    color: var(--text-muted);
    margin-bottom: 2.5rem;
}

/* Grids de Servicios y Veterinarios */
.service-grid, .vet-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
}

.card {
    background: var(--white);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: var(--card-shadow);
    text-align: center;
    padding: 2rem 1.5rem;
    transition: transform 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

.card i {
    font-size: 2.5rem;
    color: var(--primary);
    margin-bottom: 1rem;
}

.card h3 {
    margin-bottom: 0.5rem;
    font-size: 1.3rem;
}

.card p {
    color: var(--text-muted);
    font-size: 0.95rem;
}

.vet-img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 1rem;
    border: 3px solid var(--primary);
}

/* Formulario de Reserva */
.booking-card {
    background: var(--white);
    padding: 3rem;
    border-radius: 16px;
    box-shadow: var(--card-shadow);
    max-width: 800px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 1.2rem;
    text-align: left;
}

.form-group label {
    display: block;
    font-weight: 600;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
    color: var(--text-dark);
}

.form-group input, .form-group select {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 1rem;
    outline: none;
    transition: border-color 0.3s;
}

.form-group input:focus, .form-group select:focus {
    border-color: var(--primary);
}

.form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.btn-confirm {
    background-color: var(--primary);
    color: white;
    border: none;
    width: 100%;
    padding: 1rem;
    font-size: 1.1rem;
    font-weight: 600;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.3s;
    margin-top: 1rem;
}

.btn-confirm:hover {
    background-color: var(--primary-dark);
}

/* Mensaje de Confirmación */
.hidden {
    display: none;
}

#success-message {
    text-align: center;
    padding: 2rem;
}

#success-message i {
    font-size: 3rem;
    color: #2ecc71;
    margin-bottom: 1rem;
}

/* Footer */
footer {
    text-align: center;
    padding: 2rem;
    background-color: var(--text-dark);
    color: white;
    font-size: 0.9rem;
}

/* Responsive */
@media (max-width: 768px) {
    .form-row {
        grid-template-columns: 1fr;
    }
    .hero h1 {
        font-size: 2rem;
    }
}
"""

# 3. Contenido para 'script.js'
js_content = """// Datos de Servicios y Veterinarios
const servicios = [
    { 
        id: "vacuna", 
        icon: "fa-syringe", 
        title: "Vacunación y Desparasitación", 
        desc: "Protege a tu mascota manteniendo al día su carnet de vacunas y controles preventivos." 
    },
    { 
        id: "bano", 
        icon: "fa-bath", 
        title: "Baño y Estética Canina/Felina", 
        desc: "Baños especializados, corte de pelo según raza y limpieza de oídos con productos seguros." 
    },
    { 
        id: "emergencia", 
        icon: "fa-kit-medical", 
        title: "Atención de Urgencias", 
        desc: "Soporte médico rápido y diagnóstico oportuno ante cualquier imprevisto de salud." 
    }
];

const veterinarios = [
    { 
        nombre: "Dra. Sofía Morales", 
        especialidad: "Medicina General y Cirugía", 
        img: "https://images.unsplash.com/photo-1594824813563-3561a351119b?auto=format&fit=crop&w=300&q=80" 
    },
    { 
        nombre: "Dr. Carlos Mendoza", 
        especialidad: "Dermatología y Nutrición Animal", 
        img: "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=300&q=80" 
    }
];

document.addEventListener('DOMContentLoaded', () => {
    // 1. Cargar la lista de servicios en la interfaz y en el selector del formulario
    const serviceGrid = document.getElementById('service-grid');
    const serviceSelect = document.getElementById('service-select');
    
    servicios.forEach(s => {
        // Tarjeta visual de servicio
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <i class="fa-solid ${s.icon}"></i>
            <h3>${s.title}</h3>
            <p>${s.desc}</p>
        `;
        serviceGrid.appendChild(card);

        // Opción en el formulario
        const option = document.createElement('option');
        option.value = s.title;
        option.textContent = s.title;
        serviceSelect.appendChild(option);
    });

    // 2. Cargar la lista de veterinarios en la interfaz y en el selector del formulario
    const vetGrid = document.getElementById('vet-grid');
    const vetSelect = document.getElementById('vet-select');

    veterinarios.forEach(v => {
        // Tarjeta visual del veterinario
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <img src="${v.img}" alt="${v.nombre}" class="vet-img">
            <h3>${v.nombre}</h3>
            <p>${v.especialidad}</p>
        `;
        vetGrid.appendChild(card);

        // Opción en el formulario
        const option = document.createElement('option');
        option.value = v.nombre;
        option.textContent = `${v.nombre} (${v.especialidad})`;
        vetSelect.appendChild(option);
    });

    // 3. Manejo de Envío del Formulario de Cita
    const form = document.getElementById('booking-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault(); // Evita recargar la página

        const owner = document.getElementById('owner-name').value;
        const pet = document.getElementById('pet-name').value;
        const service = document.getElementById('service-select').value;
        const vet = document.getElementById('vet-select').value;
        const date = document.getElementById('appointment-date').value;
        const time = document.getElementById('appointment-time').value;

        // Ocultar el formulario y mostrar mensaje de éxito personalizado
        form.style.display = 'none';
        
        const successMsg = document.getElementById('success-message');
        const successDetails = document.getElementById('success-details');
        
        successDetails.innerHTML = `¡Gracias <strong>${owner}</strong>! La cita para tu mascota <strong>${pet}</strong> en el servicio de <strong>${service}</strong> con el/la <strong>${vet}</strong> ha quedado programada para el <strong>${date}</strong> a las <strong>${time}</strong>. Te esperamos en la clínica.`;
        successMsg.classList.remove('hidden');
    });
});
"""

# Generación física de los archivos
archivos = {
    "index.html": html_content,
    "styles.css": css_content,
    "script.js": js_content
}

for nombre_archivo, contenido in archivos.items():
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        file.write(contenido)
    print(f"✅ Archivo creado con éxito: {nombre_archivo}")

print("\n🎉 ¡Todos los archivos para 'Patitas Felices' han sido generados correctamente!")