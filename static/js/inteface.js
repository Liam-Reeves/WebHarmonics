document.addEventListener("DOMContentLoaded",()=>{
    downloadCV =>{
        const link = document.createElement('a');
        link.href = 'assets/Liam CV.pdf';
        link.download = 'Liam CV.pdf';
        document.body.appendChild(link);
       
       
    }
    
})