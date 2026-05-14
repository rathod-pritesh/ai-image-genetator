<script>
  export let loading = false;
  export let imageBase64 = "";
  export let handleDownload;
</script>

<div class="mt-8 flex flex-col items-center">
  {#if loading}
    <div
      class="w-full aspect-square bg-gray-100 animate-pulse rounded-xl flex items-center justify-center"
    >
      <p class="text-gray-400 font-medium">Forging your masterpiece...</p>
    </div>
  {/if}

  {#if imageBase64}
    <div class="group relative w-full">
      <img
        src={"data:image/jpeg;base64," + imageBase64}
        alt="Generated Art"
        class="w-full h-auto rounded-xl shadow-lg border border-gray-200 transition-transform duration-300 hover:scale-[1.01]"
      />
      <div
        class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 rounded-xl flex items-center justify-center transition-opacity"
      >
        <button
          on:click={handleDownload}
          class="bg-white text-gray-900 px-4 py-2 rounded-lg font-semibold text-sm"
          >Download Image</button
        >
      </div>
    </div>
  {/if}
</div>
