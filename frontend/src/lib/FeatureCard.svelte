<script>
  export let number = "";
  export let title = "";
  export let description = "";
</script>

<div
  class="p-6 bg-white rounded-xl shadow-sm border border-gray-50 text-center"
>
  <div
    class="w-12 h-12 bg-indigo-100 text-indigo-600 rounded-lg flex items-center justify-center mx-auto mb-4 font-bold text-xl"
  >
    {number}
  </div>
  <h3 class="font-bold text-gray-900 mb-2">{title}</h3>
  <p class="text-sm text-gray-600">{description}</p>
</div>
