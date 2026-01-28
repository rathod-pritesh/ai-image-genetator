<script>
  let prompt = "";
  let imageBase64 = "";
  let loading = false;

  async function generateImage() {
    if (!prompt) return;

    loading = true;
    imageBase64 = "";

    const res = await fetch("http://127.0.0.1:8000/generate-image", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    });

    const data = await res.json();

    imageBase64 = data.image_base64;

    loading = false;

    console.log(data);
  }
  function handleDownload() {
    if (!imageBase64) return;

    const link = document.createElement("a");

    link.href = `data:image/jpeg;base64, ${imageBase64}`;

    const fileName = prompt
      ? prompt.slice(0, 20).replace(/[^a-z0-9]/gi, '_').toLowerCase()
      : "ai-generated-image";

    link.download = `${fileName}.webp`;

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
</script>

<div class="min-h-screen bg-gray-50 flex flex-col items-center p-4 md:p-8">
  <header class="w-full max-w-2xl text-center mb-10 mt-8">
    <h1 class="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tight">AI Image 
      <span class="text-indigo-600">Generator</span>
    </h1>
    <p class="mt-3 text-gray-600">Turn your imagination into art in seconds.</p>
  </header>

  <main class="w-full max-w-xl bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
    <div class="flex flex-col gap-4">
    <div class="flex flex-col gap-2">
      <label for="prompt" class="text-sm font-semibold text-gray-700">Prompt</label>
      <textarea 
        id="prompt"
        rows="3"
        class="w-full border border-gray-300 rounded-xl px-4 py-3 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all outline-none resize-none"
        placeholder="Describe your image..."
        bind:value={prompt}
      ></textarea>
    </div>

    <button
      class="w-full bg-indigo-600 hover:bg-indigo-700 disabled:bg-indigo-300 text-white font-bold py-3 px-6 rounded-xl transition-colors flex items-center justify-center gap-2"
      on:click={generateImage}
      disabled={loading || !prompt}
    >
      {#if loading}
        <span class="animate-spin border-2 border-white border-t-transparent rounded-full w-5 h-5"></span>
        Generating...
      {:else}
        Generate Image
      {/if}
    </button>
  </div>

  <div class="mt-8 flex flex-col items-center">
    {#if loading}
      <div class="w-full aspect-square bg-gray-100 animate-pulse rounded-xl flex items-center justify-center">
        <p class="text-gray-400 font-medium">Processing your prompt...</p>
      </div>
    {/if}

    {#if imageBase64}
      <div class="group relative w-full">
        <img 
          src={"data:image/jpeg;base64," + imageBase64} 
          alt="Generated Art"
          class="w-full h-auto rounded-xl shadow-lg border border-gray-200 transition-transform duration-300 hover:scale-[1.01]"
        />
        <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 rounded-xl flex items-center justify-center">
          <button on:click={handleDownload} class="bg-white text-gray-900 px-4 py-2 roudned-lg font-semibold text-sm">Download</button>
        </div>
      </div>
    {/if}
  </div>
  </main>

</div>