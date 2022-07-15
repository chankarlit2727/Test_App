// const postList = document.querySelector('.link-list')
// let output = '';

// const url = 'http://localhost:8000/urlInput';

// fetch(url)
//     .then(res => res.json())
//     .then(data =>{
//         data.forEach(post => {
//             output += `
//             <div>
//                 <span><a href="createLink/" class="btn btn-primary btn-lg">Add new link</a></span>
//             </div>
//             <br>
//             <table data-toggle="table">
//             <thead>
//                 <tr>
//                 <th scope="col">URL's</th>
//                 <th scope="col">Status</th>
//                 <th scope="col"></th>
//                 <th scope="col"></th>
//                 </tr>
//             </thead>
//             <tbody id="display">
                
//             </tbody>
//             </table>
//             `;
//         });
//         postList.innerHTML = output;
//     })