<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Complaint;
use Illuminate\Http\Request;

class ComplaintController extends Controller
{
    public function index()
    {
        return response()->json(Complaint::with('facility')->get(), 200);
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'facility_id' => 'required|exists:facilities,id',
            'title' => 'required|string|max:255',
            'description' => 'required|string',
            'status' => 'nullable|string|max:255',
        ]);

        $complaint = Complaint::create($validated);
        return response()->json($complaint, 201);
    }

    public function show($id)
    {
        $complaint = Complaint::with('facility')->find($id);
        if (!$complaint) {
            return response()->json(['message' => 'Complaint not found'], 404);
        }
        return response()->json($complaint, 200);
    }

    public function update(Request $request, $id)
    {
        $complaint = Complaint::find($id);
        if (!$complaint) {
            return response()->json(['message' => 'Complaint not found'], 404);
        }

        $validated = $request->validate([
            'facility_id' => 'required|exists:facilities,id',
            'title' => 'required|string|max:255',
            'description' => 'required|string',
            'status' => 'nullable|string|max:255',
        ]);

        $complaint->update($validated);
        return response()->json($complaint, 200);
    }

    public function destroy($id)
    {
        $complaint = Complaint::find($id);
        if (!$complaint) {
            return response()->json(['message' => 'Complaint not found'], 404);
        }

        $complaint->delete();
        return response()->json(['message' => 'Complaint deleted successfully'], 200);
    }
}
