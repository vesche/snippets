using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UIManager : MonoBehaviour {

	public Slider healthBar;
	public Text HPText;
	public PlayerHealthManager playerHealth;

	private static bool UIExists;

	private PlayerStats thePS;
	public Text levelText;


	// Use this for initialization
	void Start () {

		if (!UIExists) 
		{
			UIExists = true;
			// FOLLOW TO NEW SCENES
			DontDestroyOnLoad (transform.gameObject);

		} else {
			Destroy (gameObject);
		}

		thePS = GetComponent<PlayerStats> ();

	}
	
	// Update is called once per frame
	void Update () {
		healthBar.maxValue = playerHealth.playerMaxHealth;
		healthBar.value = playerHealth.playerCurrentHealth;
		HPText.text = "HP: " + playerHealth.playerCurrentHealth + "/" + playerHealth.playerMaxHealth;
		levelText.text = "Lvl: " + thePS.currentLevel;
	}
}
