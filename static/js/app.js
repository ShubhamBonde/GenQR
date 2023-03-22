function addInteractivity() {
    // Closure
    const hamMenu = document.querySelector('.hamburger-menu')
    const navMobile = document.querySelector('.nav-links-mobile') 
    const backDrop = document.querySelector('.back-drop');
    const flashMsg = document.querySelector('.flash-msg')
    function runner() {
        hamMenu.addEventListener('click', ()=> {
            if (hamMenu.classList.contains('active')) {
                hamMenu.classList.toggle('inactive')

            }
            else hamMenu.classList.toggle('active');
            navMobile.classList.toggle('active')
            backDrop.classList.toggle('inactive')
        })

        setInterval(()=> {
            if (flashMsg !== null) flashMsg.classList.add('delete');
        }, 5000)
    }
    return runner;
}





const app = addInteractivity()
app()

// function qrIpHandler(value) {
//     let qrData = new FormData()
//     qrData.append('qrtext', value);

//     let data = fetch('http://127.0.0.1:8000/generated-qr', {
//         method: "POST",
//         body: qrData
//     })

//     data.then((res)=> {
//         res.body.getReader().read().then(img => {
//             let qrByteArr = img.value;
//             let stringValue = String.fromCharCode(...qrByteArr)
//             let encodedValue = btoa(stringValue)
//             document.querySelector('.generated_qr').src = `data:image/png;base64,${encodedValue}`
//         })
//     })
// }
