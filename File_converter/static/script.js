function convertFile(endpoint) {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        console.error('No file selected.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch(`/${endpoint}`, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to convert file.');
        }
        return response.blob();
    })
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = `${file.name.replace(/\.\w+$/, '')}.${endpoint.split('-').pop()}`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        
        document.getElementById('result').innerHTML = `<p>File converted successfully! <a href="${url}" download="${a.download}">Download</a></p>`;
    })
    .catch(error => {
        console.error('Error converting file:', error);
        document.getElementById('result').innerHTML = '<p style="color: red;">Error converting file. Please try again.</p>';
    });
}

function adjustFileSize(action) {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        console.error('No file selected.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch(`/${action}-file-size`, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Failed to ${action} file size.`);
        }
        return response.blob();
    })
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = `modified_${file.name}`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);

        document.getElementById('result').innerHTML = `<p>File size ${action}d successfully! <a href="${url}" download="${a.download}">Download</a></p>`;
    })
    .catch(error => {
        console.error(`Error ${action}ing file size:`, error);
        document.getElementById('result').innerHTML = `<p style="color: red;">Error ${action}ing file size. Please try again.</p>`;
    });
}
