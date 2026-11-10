// Datos de Servicios y Veterinarios
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
