// QR Code Display functionality
document.addEventListener('DOMContentLoaded', function() {
    loadQRCode();
    setupEventListeners();
});

function loadQRCode() {
    const qrImageData = sessionStorage.getItem('qrImageData');
    const userData = sessionStorage.getItem('userData');
    
    console.log('Loading QR code...');
    console.log('Has image data:', !!qrImageData);
    console.log('Has user data:', !!userData);
    
    if (!qrImageData || !userData) {
        console.log('Missing data, redirecting to generator');
        window.location.href = 'genqr.html';
        return;
    }
    
    // Display the QR code using the stored base64 data
    const qrImage = document.getElementById('qrImage');
    qrImage.src = qrImageData;
    
    qrImage.onload = function() {
        console.log('QR image displayed successfully');
    };
    
    qrImage.onerror = function() {
        console.error('Failed to display QR image');
        showMessage('Failed to load QR code image');
    };
    
    // Display user information
    const userInfo = document.getElementById('userInfo');
    const user = JSON.parse(userData);
    
    userInfo.innerHTML = `
        <h4>Generated for:</h4>
        <p><strong>Name:</strong> ${user.first_name} ${user.last_name}</p>
        <p><strong>Email:</strong> ${user.email}</p>
        <p><strong>Student ID:</strong> ${user.student_id}</p>
        <p><strong>Standard:</strong> ${user.standard}</p>
        <p><strong>Stream/Section:</strong> ${user.streamORsection}</p>
    `;
}

function setupEventListeners() {
    const downloadBtn = document.getElementById('downloadBtn');
    const generateNewBtn = document.getElementById('generateNewBtn');
    
    if (downloadBtn) downloadBtn.addEventListener('click', downloadQRCode);
    if (generateNewBtn) generateNewBtn.addEventListener('click', generateNewQR);
}

function downloadQRCode() {
    console.log('Download button clicked');
    const userData = JSON.parse(sessionStorage.getItem('userData'));
    const qrImageData = sessionStorage.getItem('qrImageData');
    
    if (!qrImageData) {
        showMessage('No QR code available for download');
        return;
    }
    
    try {
        // Create download link from base64 data
        const link = document.createElement('a');
        link.href = qrImageData;
        link.download = `${userData.first_name}_${userData.last_name}_QR.png`;
        
        // Trigger download
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        
        showMessage('QR code downloaded successfully!');
    } catch (error) {
        console.error('Error downloading QR code:', error);
        showMessage('Failed to download QR code. Please try again.');
    }
}

function generateNewQR() {
    console.log('Generate new QR button clicked');
    // Clear stored data and redirect
    sessionStorage.removeItem('qrImageData');
    sessionStorage.removeItem('userData');
    window.location.href = 'genqr.html';
}

function showMessage(message) {
    console.log('Showing message:', message);
    let messageDiv = document.getElementById('shareMessage');
    if (!messageDiv) {
        messageDiv = document.createElement('div');
        messageDiv.id = 'shareMessage';
        messageDiv.className = 'success-message';
        const container = document.querySelector('.qr-display-section .feature-card');
        if (container) {
            container.appendChild(messageDiv);
        }
    }
    
    messageDiv.textContent = message;
    messageDiv.style.display = 'block';
    
    setTimeout(() => {
        messageDiv.style.display = 'none';
    }, 3000);
}