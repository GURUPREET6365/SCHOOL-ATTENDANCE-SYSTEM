// View QR Code functionality
let currentStudentId = null;
let currentQrImageData = null;

document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
});

function setupEventListeners() {
    const viewQrForm = document.getElementById('viewQrForm');
    const downloadBtn = document.getElementById('downloadBtn');
    const searchNewBtn = document.getElementById('searchNewBtn');
    
    if (viewQrForm) viewQrForm.addEventListener('submit', handleViewQrSubmit);
    if (downloadBtn) downloadBtn.addEventListener('click', downloadQRCode);
    if (searchNewBtn) searchNewBtn.addEventListener('click', searchNewQR);
}

async function handleViewQrSubmit(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    const studentId = formData.get('student_id');
    
    if (!studentId) {
        showError('Please enter a student ID');
        return;
    }
    
    currentStudentId = studentId;
    
    // Show loading state and hide any previous QR display
    showLoading(true);
    hideQrDisplay();

    try {
        const response = await fetch(`http://127.0.0.1:8000/api/view/QRcode/${studentId}`, {
            method: 'GET'
        });

        if (!response.ok) {
            // Handle HTTP errors and extract detail from HTTPException
            let errorMessage = `HTTP error! status: ${response.status}`;
            
            try {
                const errorData = await response.json();
                if (errorData.detail) {
                    errorMessage = errorData.detail;
                } else if (errorData.message) {
                    errorMessage = errorData.message;
                }
            } catch (parseError) {
                console.log('Could not parse error response as JSON');
            }
            
            // Don't show QR display section on error
            hideQrDisplay();
            throw new Error(errorMessage);
        }

        // Get the image blob
        const imageBlob = await response.blob();
        console.log('QR code image received, size:', imageBlob.size);
        
        // Convert blob to base64 data URL for storage
        const reader = new FileReader();
        reader.onload = function() {
            currentQrImageData = reader.result;
            console.log('QR code converted to base64');
            
            // Only display the QR code if conversion was successful
            displayQrCode();
        };
        
        reader.onerror = function() {
            // Hide QR display on conversion error
            hideQrDisplay();
            throw new Error('Failed to process QR code image');
        };
        
        // Convert to base64
        reader.readAsDataURL(imageBlob);
        
    } catch (error) {
        console.error('Error viewing QR code:', error);
        // Ensure QR display is hidden on any error
        hideQrDisplay();
        showError(error.message);
    } finally {
        showLoading(false);
    }
}

function displayQrCode() {
    const qrImage = document.getElementById('qrImage');
    const studentInfo = document.getElementById('studentInfo');
    const qrDisplaySection = document.getElementById('qrDisplaySection');
    
    // Only proceed if we have valid QR data
    if (!currentQrImageData || !currentStudentId) {
        console.error('Missing QR data, cannot display');
        hideQrDisplay();
        return;
    }
    
    // Set the QR code image
    qrImage.src = currentQrImageData;
    
    qrImage.onload = function() {
        console.log('QR code displayed successfully');
        // Only show the display section after image loads successfully
        qrDisplaySection.style.display = 'block';
        // Scroll to the QR code section
        qrDisplaySection.scrollIntoView({ behavior: 'smooth' });
    };
    
    qrImage.onerror = function() {
        console.error('Failed to display QR code');
        hideQrDisplay();
        showError('Failed to load QR code image');
    };
    
    // Display student information
    studentInfo.innerHTML = `
        <h4>QR Code Details:</h4>
        <p><strong>Student ID:</strong> ${currentStudentId}</p>
    `;
}

function hideQrDisplay() {
    const qrDisplaySection = document.getElementById('qrDisplaySection');
    qrDisplaySection.style.display = 'none';
}

function downloadQRCode() {
    console.log('Download button clicked');
    
    if (!currentQrImageData || !currentStudentId) {
        showMessage('No QR code available for download');
        return;
    }
    
    try {
        // Create download link from base64 data
        const link = document.createElement('a');
        link.href = currentQrImageData;
        link.download = `Student_${currentStudentId}_QR.png`;
        
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

function searchNewQR() {
    console.log('Search new QR button clicked');
    // Clear current data
    currentStudentId = null;
    currentQrImageData = null;
    
    // Hide QR display section
    hideQrDisplay();
    
    // Clear the form
    const form = document.getElementById('viewQrForm');
    if (form) {
        form.reset();
    }
    
    // Scroll back to the search form
    const searchSection = document.querySelector('.qr-search-section');
    if (searchSection) {
        searchSection.scrollIntoView({ behavior: 'smooth' });
    }
}

function showLoading(show) {
    const loading = document.getElementById('loading');
    const form = document.getElementById('viewQrForm');
    
    if (show) {
        loading.style.display = 'block';
        form.style.opacity = '0.5';
        form.style.pointerEvents = 'none';
    } else {
        loading.style.display = 'none';
        form.style.opacity = '1';
        form.style.pointerEvents = 'auto';
    }
}

function showError(message) {
    // Create or update error message
    let errorDiv = document.getElementById('errorMessage');
    if (!errorDiv) {
        errorDiv = document.createElement('div');
        errorDiv.id = 'errorMessage';
        errorDiv.className = 'error-message';
        document.querySelector('.qr-search-section .feature-card').appendChild(errorDiv);
    }
    
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    
    // Hide error after 5 seconds
    setTimeout(() => {
        errorDiv.style.display = 'none';
    }, 5000);
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