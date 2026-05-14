<script>
  import Generator from '$lib/Generator.svelte';
  import ImageDisplay from '$lib/ImageDisplay.svelte';
  import FeatureCard from '$lib/FeatureCard.svelte';
  import Logo from '$lib/ai-image-generator-logo.png';

  let prompt = "";
  let imageBase64 = "";
  let loading = false;
  let error = "";

  async function generateImage() {
    if (!prompt || loading) return;
    loading = true;
    error = "";
    imageBase64 = "";

    try {
      const res = await fetch("http://127.0.0.1:8000/generate-image", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt })
      });

      if (!res.ok) throw new Error("The forge is currently cold. Please try again later.");

      const data = await res.json();
      imageBase64 = data.image_base64;
      prompt = ""; 
    } catch (err) {
      error = "Connection lost: The AI service is currently unavailable.";
    } finally {
      loading = false;
    }
  }

  function handleKeyDown(event) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      generateImage();
    }
  }

  function handleDownload() {
    if (!imageBase64) return;
    const link = document.createElement("a");
    link.href = `data:image/jpeg;base64, ${imageBase64}`;
    link.download = `pixelforge-${Date.now()}.webp`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
</script>

<nav class="w-full bg-white border-b border-gray-100 py-6 px-6 md:px-12 flex justify-between items-center">
  <div class="flex items-center">
    <img src={Logo} alt="PixelForge Logo" class="h-20 md:h-24 w-auto object-contain" />
  </div>
  <div class="hidden md:flex gap-8 text-sm font-semibold text-gray-600 uppercase tracking-wider">
    <a href="#generate" class="hover:text-indigo-600 transition-colors border-b-2 border-indigo-600 pb-1">Generator</a>
    <a href="#how-it-works" class="hover:text-indigo-600 transition-colors pb-1">How it Works</a>
  </div>
</nav>

<div id="generate" class="min-h-screen bg-gray-50 flex flex-col items-center p-4 md:p-8">
  <header class="w-full max-w-2xl text-center mb-10 mt-8">
    <h1 class="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tight">
      AI Image <span class="text-indigo-600">Generator</span>
    </h1>
    <p class="mt-3 text-gray-600 italic">"Where imagination meets the forge."</p>
  </header>

  <main class="w-full max-w-xl bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
    <!-- Generator Component -->
    <Generator 
      bind:prompt 
      {loading} 
      {error} 
      {generateImage} 
      {handleKeyDown} 
    />

    <!-- Image Display Component -->
    <ImageDisplay 
      {loading} 
      {imageBase64} 
      {handleDownload} 
    />
  </main>

  <section id="how-it-works" class="w-full max-w-4xl mt-20 mb-20">
    <div class="text-center mb-12">
        <h2 class="text-2xl font-bold text-gray-900">The PixelForge Process</h2>
        <p class="text-gray-500">Fast, high-quality, and powered by Pollinations.ai</p>
    </div>
    <div class="grid md:grid-cols-3 gap-8">
      <FeatureCard 
        number="1" 
        title="Input Prompt" 
        description="Enter your vision into the forge's text field." 
      />
      <FeatureCard 
        number="2" 
        title="Forge" 
        description="The AI strikes the pixels to create your unique artwork." 
      />
      <FeatureCard 
        number="3" 
        title="Download" 
        description="Grab your creation and share it with the world." 
      />
    </div>
  </section>

  <footer class="text-gray-400 text-sm pb-8">
    &copy; 2026 PixelForge Studio | Powered by Pollinations AI
  </footer>
</div>