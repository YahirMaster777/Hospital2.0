<template>
<!-- https://play.tailwindcss.com/MIwj5Sp9pw -->

<div class="p-20 w-full min-h-screen bg-gray-700 bg-center">
    <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-4xl">
        <div class="hidden lg:block lg:w-1/2 bg-cover"
            style="background-image:url('https://scontent.fmex19-1.fna.fbcdn.net/v/t31.18172-8/1272393_10151640751062957_1026130586_o.jpg?_nc_cat=104&ccb=1-7&_nc_sid=5f2048&_nc_ohc=TEjI7lHRp4kQ7kNvgHDyUeq&_nc_ht=scontent.fmex19-1.fna&oh=00_AYAmX3fu3fQ-KBNxkknaDdduJZvN0n_zBwTpA9d7iwn1Rg&oe=6689A015')">
        </div>
        <div class="w-max p-8 lg:w-1/2 bg-gray-800">
            <h2 class="text-2xl font-semibold text-white text-center">Iniciar Sesion</h2>
            
            
            <div class="mt-4">
                <label class="block text-white text-sm font-bold mb-2">Direccion de Correo electronico</label>
                <input class="bg-gray-200 text-white focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="email" />
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-white text-sm font-bold mb-2">Contraseña</label>
                    
                </div>
                <input class="bg-gray-200 text-white focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="password" />
            </div>
            <a href="#" class="text-xs text-blue-600">Olvidaste tu Contraseña?</a>
            <div class="mt-8">
                <router-link to="/dashboard">
                <button class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600">Iniciar Sesion</button>
                </router-link> 
            </div>

            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 lg:w-1/4"></span>
                <a href="#" class="text-xs text-center text-gray-500 uppercase">O inicia con otra cuenta</a>
                <span class="border-b w-1/5 lg:w-1/4"></span>
            </div>

            <a href="#" class="flex items-center justify-center mt-4 text-white rounded-lg shadow-md hover:bg-gray-100">
                            <div class="px-4 py-3 bg-white ">
                                <svg class="h-6 w-6" viewBox="0 0 40 40">
                                    <path
                                        d="M36.3425 16.7358H35V16.6667H20V23.3333H29.4192C28.045 27.2142 24.3525 30 20 30C14.4775 30 10 25.5225 10 20C10 14.4775 14.4775 9.99999 20 9.99999C22.5492 9.99999 24.8683 10.9617 26.6342 12.5325L31.3483 7.81833C28.3717 5.04416 24.39 3.33333 20 3.33333C10.7958 3.33333 3.33335 10.7958 3.33335 20C3.33335 29.2042 10.7958 36.6667 20 36.6667C29.2042 36.6667 36.6667 29.2042 36.6667 20C36.6667 18.8825 36.5517 17.7917 36.3425 16.7358Z"
                                        fill="#FFC107" />
                                    <path
                                        d="M5.25497 12.2425L10.7308 16.2583C12.2125 12.59 15.8008 9.99999 20 9.99999C22.5491 9.99999 24.8683 10.9617 26.6341 12.5325L31.3483 7.81833C28.3716 5.04416 24.39 3.33333 20 3.33333C13.5983 3.33333 8.04663 6.94749 5.25497 12.2425Z"
                                        fill="#FF3D00" />
                                    <path
                                        d="M20 36.6667C24.305 36.6667 28.2167 35.0192 31.1742 32.34L26.0159 27.975C24.3425 29.2425 22.2625 30 20 30C15.665 30 11.9842 27.2359 10.5975 23.3784L5.16254 27.5659C7.92087 32.9634 13.5225 36.6667 20 36.6667Z"
                                        fill="#4CAF50" />
                                    <path
                                        d="M36.3425 16.7358H35V16.6667H20V23.3333H29.4192C28.7592 25.1975 27.56 26.805 26.0133 27.9758C26.0142 27.975 26.015 27.975 26.0158 27.9742L31.1742 32.3392C30.8092 32.6708 36.6667 28.3333 36.6667 20C36.6667 18.8825 36.5517 17.7917 36.3425 16.7358Z"
                                        fill="#1976D2" />
                                </svg>
                            </div>
                            <h1  class="px-4 py-3 w-5/6 text-center text-gray-600 font-bold bg-white">Inicia con Google</h1>
                        </a>
                        <div class="mt-3">
                <router-link to="/register">
                <button class="bg-gray-500 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600">Registrarse</button>
                </router-link> 
            </div>


           
        </div>
    </div>
</div>
</template>
