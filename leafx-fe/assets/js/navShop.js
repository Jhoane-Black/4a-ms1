/*=============== Draggable and Resizable ===============*/

const el = document.querySelector('.item');
let isResizing = false;

el.addEventListener('mousedown', mousedown);

function mousedown(e) {

    window.addEventListener('mousemove', mousemove);
    window.addEventListener('mouseup'  , mouseup);

    let prevX = e.clientX;
    let prevY = e.clientY;

    function mouseup() {
        window.removeEventListener('mouseup'  , mouseup);
        window.removeEventListener('mousemove', mousemove);
    }

    function mousemove(e) {
        
        if (!isResizing) {

            let newX = prevX - e.clientX;
            let newY = prevY - e.clientY;

            const rect = el.getBoundingClientRect();

            el.style.left = rect.left - newX + 'px';
            el.style.top  = rect.top  - newY + 'px';

            prevX = e.clientX;
            prevY = e.clientY;

        }

    }

}

const resizers = document.querySelectorAll('.resizer');
let currentResizer;

for (resizer of resizers) {

   resizer.addEventListener('mousedown', mousedown);

    function mousedown(e) {

        isResizing = true;

        currentResizer = e.target;

        let prevX = e.clientX;
        let prevY = e.clientY;

        window.addEventListener('mousemove', mousemove);
        window.addEventListener('mouseup'  , mouseup);

        function mousemove (e) {

            const rect = el.getBoundingClientRect();

            if (currentResizer.classList.contains('se')) {

                el.style.width  = rect.width  - (prevX - e.clientX) + 'px';
                el.style.height = rect.height - (prevY - e.clientY) + 'px';
    
            } else if (currentResizer.classList.contains('sw')) {

                el.style.width  = rect.width  + (prevX - e.clientX) + 'px';
                el.style.height = rect.height - (prevY - e.clientY) + 'px';
                el.style.left   = rect.left   - (prevX - e.clientX) + 'px';

            } else if (currentResizer.classList.contains('nw')) {

                el.style.width  = rect.width  + (prevX - e.clientX) + 'px';
                el.style.height = rect.height + (prevY - e.clientY) + 'px';
                el.style.left   = rect.left   - (prevX - e.clientX) + 'px';
                el.style.top    = rect.top    - (prevY - e.clientY) + 'px';

            } else if (currentResizer.classList.contains('ne')) {

                el.style.width  = rect.width  - (prevX - e.clientX) + 'px';
                el.style.height = rect.height + (prevY - e.clientY) + 'px';
                el.style.top    = rect.top    - (prevY - e.clientY) + 'px';

            }

            prevX = e.clientX;
            prevY = e.clientY;

        }

        function mouseup() {

            window.removeEventListener('mouseup'  , mouseup);
            window.removeEventListener('mousemove', mousemove);

            isResizing = false;

        }

    }

}