modal = document.getElementById('modal')
content = document.getElementById('modal-content')



function openModal(){
    modal.classList.remove('hidden')
    modal.classList.add('flex')

    setTimeout(()=>{
        content.classList.remove('scale-95', 'opacity-95')
    }, 10)
    
}
function closeModal(){
    content.classList.add('scale-95', 'opacity-95')
    
    setTimeout(()=>{
        modal.classList.add('hidden')
        modal.classList.remove('flex')
    }, 200)
}

modal.addEventListener('click', (e)=>{
    if(e.target.id === 'modal') closeModal()
})
