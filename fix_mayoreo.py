import re

html_path = 'nueva_web_pruebas/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_mayoreo = """      <div class="overflow-x-auto w-full mb-8">
        <table class="w-full text-left bg-white rounded-lg shadow-sm overflow-hidden min-w-[600px]">
          <thead class="bg-deep-teal text-white">
            <tr>
              <th class="p-4 font-semibold">Forma</th>
              <th class="p-4 font-semibold">Tamaño</th>
              <th class="p-4 font-semibold">100+ unidades</th>
              <th class="p-4 font-semibold">500+ unidades</th>
                          </tr>
          </thead>
          <tbody class="divide-y divide-gray-100">
            <tr class="hover:bg-gray-50"><td class="p-4">Circular / Cuadrada</td><td class="p-4 font-medium text-deep-teal">4.0 cm</td><td class="p-4">$18</td><td class="p-4">$17</td></tr>
            <tr class="hover:bg-gray-50"><td class="p-4">Circular / Cuadrada</td><td class="p-4 font-medium text-deep-teal">5.0 cm</td><td class="p-4">$23</td><td class="p-4">$22</td></tr>
            <tr class="hover:bg-gray-50"><td class="p-4">Circular / Cuadrada</td><td class="p-4 font-medium text-deep-teal">7.5 cm</td><td class="p-4">$38</td><td class="p-4">$37</td></tr>
            <tr class="hover:bg-gray-50"><td class="p-4">Circular / Cuadrada</td><td class="p-4 font-medium text-deep-teal">8.5 cm</td><td class="p-4">$43</td><td class="p-4">$42</td></tr>
            <tr class="hover:bg-gray-50"><td class="p-4">Rectangular</td><td class="p-4 font-medium text-deep-teal">6.0 × 4.5 cm</td><td class="p-4">$24</td><td class="p-4">$23</td></tr>
            <tr class="hover:bg-gray-50"><td class="p-4">Rectangular</td><td class="p-4 font-medium text-deep-teal">7.5 × 5.5 cm</td><td class="p-4">$34</td><td class="p-4">$33</td></tr>
          </tbody>
        </table>
      </div>"""

new_mayoreo = """      <div class="space-y-12 mb-12">
        <!-- Grupo Circular / Cuadrada -->
        <div>
          <h3 class="text-2xl font-semibold text-terracotta mb-6 border-b border-terracotta/20 pb-2">Forma Circular / Cuadrada</h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- Card 4.0 -->
            <div class="bg-white p-6 rounded-lg ambient-shadow border border-gray-100 hover:border-terracotta/30 transition-colors">
              <div class="text-3xl font-bold text-deep-teal mb-1">4.0 <span class="text-lg text-on-surface-variant font-normal">cm</span></div>
              <div class="w-8 h-1 bg-terracotta/40 mb-4 rounded-full"></div>
              <div class="flex justify-between items-center py-2 border-b border-gray-50">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">100+ pz</span>
                <span class="text-lg font-bold text-deep-teal">$18</span>
              </div>
              <div class="flex justify-between items-center py-2">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">500+ pz</span>
                <span class="text-lg font-bold text-terracotta">$17</span>
              </div>
            </div>
            <!-- Card 5.0 -->
            <div class="bg-white p-6 rounded-lg ambient-shadow border border-gray-100 hover:border-terracotta/30 transition-colors">
              <div class="text-3xl font-bold text-deep-teal mb-1">5.0 <span class="text-lg text-on-surface-variant font-normal">cm</span></div>
              <div class="w-8 h-1 bg-terracotta/40 mb-4 rounded-full"></div>
              <div class="flex justify-between items-center py-2 border-b border-gray-50">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">100+ pz</span>
                <span class="text-lg font-bold text-deep-teal">$23</span>
              </div>
              <div class="flex justify-between items-center py-2">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">500+ pz</span>
                <span class="text-lg font-bold text-terracotta">$22</span>
              </div>
            </div>
            <!-- Card 7.5 -->
            <div class="bg-white p-6 rounded-lg ambient-shadow border border-gray-100 hover:border-terracotta/30 transition-colors">
              <div class="text-3xl font-bold text-deep-teal mb-1">7.5 <span class="text-lg text-on-surface-variant font-normal">cm</span></div>
              <div class="w-8 h-1 bg-terracotta/40 mb-4 rounded-full"></div>
              <div class="flex justify-between items-center py-2 border-b border-gray-50">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">100+ pz</span>
                <span class="text-lg font-bold text-deep-teal">$38</span>
              </div>
              <div class="flex justify-between items-center py-2">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">500+ pz</span>
                <span class="text-lg font-bold text-terracotta">$37</span>
              </div>
            </div>
            <!-- Card 8.5 -->
            <div class="bg-white p-6 rounded-lg ambient-shadow border border-gray-100 hover:border-terracotta/30 transition-colors">
              <div class="text-3xl font-bold text-deep-teal mb-1">8.5 <span class="text-lg text-on-surface-variant font-normal">cm</span></div>
              <div class="w-8 h-1 bg-terracotta/40 mb-4 rounded-full"></div>
              <div class="flex justify-between items-center py-2 border-b border-gray-50">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">100+ pz</span>
                <span class="text-lg font-bold text-deep-teal">$43</span>
              </div>
              <div class="flex justify-between items-center py-2">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">500+ pz</span>
                <span class="text-lg font-bold text-terracotta">$42</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Grupo Rectangular -->
        <div>
          <h3 class="text-2xl font-semibold text-terracotta mb-6 border-b border-terracotta/20 pb-2">Forma Rectangular</h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- Card 6.0 x 4.5 -->
            <div class="bg-white p-6 rounded-lg ambient-shadow border border-gray-100 hover:border-terracotta/30 transition-colors">
              <div class="text-3xl font-bold text-deep-teal mb-1">6<span class="text-lg font-normal mx-1">×</span>4.5 <span class="text-lg text-on-surface-variant font-normal">cm</span></div>
              <div class="w-8 h-1 bg-terracotta/40 mb-4 rounded-full"></div>
              <div class="flex justify-between items-center py-2 border-b border-gray-50">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">100+ pz</span>
                <span class="text-lg font-bold text-deep-teal">$24</span>
              </div>
              <div class="flex justify-between items-center py-2">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">500+ pz</span>
                <span class="text-lg font-bold text-terracotta">$23</span>
              </div>
            </div>
            <!-- Card 7.5 x 5.5 -->
            <div class="bg-white p-6 rounded-lg ambient-shadow border border-gray-100 hover:border-terracotta/30 transition-colors">
              <div class="text-3xl font-bold text-deep-teal mb-1">7.5<span class="text-lg font-normal mx-1">×</span>5.5 <span class="text-lg text-on-surface-variant font-normal">cm</span></div>
              <div class="w-8 h-1 bg-terracotta/40 mb-4 rounded-full"></div>
              <div class="flex justify-between items-center py-2 border-b border-gray-50">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">100+ pz</span>
                <span class="text-lg font-bold text-deep-teal">$34</span>
              </div>
              <div class="flex justify-between items-center py-2">
                <span class="text-sm font-medium text-on-surface-variant uppercase tracking-wider">500+ pz</span>
                <span class="text-lg font-bold text-terracotta">$33</span>
              </div>
            </div>
          </div>
        </div>
      </div>"""

html = html.replace(old_mayoreo, new_mayoreo)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Mayoreo section redesigned!")
